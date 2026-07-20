---
title: "[Solution] Java IIFImageRankException — Invalid Image Band Rank"
description: "Fix Java IIFImageRankException by verifying image bands, checking sample model, and validating image structure before processing."
languages: ["java"]
severities: ["error"]
error_types: ["runtime"]
weight: 20
---

# IIFImageRankException — Invalid Image Band Rank

An `IIFImageRankException` is thrown when an image band rank is invalid or when the image's band structure does not match expected parameters. This is an internal exception in the `javax.imageio` framework, typically encountered during image processing operations.

## Description

`IIFImageRankException` (ImageIO Internal Framework Image Rank Exception) indicates a mismatch between the image's band rank (number of bands and their ordering) and the operation being performed. This can occur when combining images with different band structures or when using image writers/readers that expect specific band configurations.

Common message variants:

- `javax.imageio.IIFImageRankException: Image rank mismatch`
- `javax.imageio.IIFImageRankException: Invalid number of bands`
- `javax.imageio.IIFImageRankException: Band mismatch between source and destination`

## Common Causes

```java
// Cause 1: Mismatched band count in image combination
BufferedImage rgb = new BufferedImage(100, 100, BufferedImage.TYPE_INT_RGB);
BufferedImage rgba = new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB);
// Combining these may cause IIFImageRankException

// Cause 2: Using wrong SampleModel for image type
int[] data = new int[100 * 100 * 3];
SampleModel model = new PixelInterleavedSampleModel(
    DataBuffer.TYPE_INT, 100, 100, 3, 300, new int[]{0, 1, 2}
);
DataBufferInt buffer = new DataBufferInt(data, data.length);
Raster raster = Raster.createRaster(model, buffer, null);
// May fail if band rank is inconsistent

// Cause 3: Writing image with incompatible bands
BufferedImage src = new BufferedImage(100, 100, BufferedImage.TYPE_3BYTE_BGR);
ImageWriter writer = ImageIO.getImageWritersByFormatName("jpg").next();
ImageWriteParam param = writer.getDefaultWriteParam();
// Writing with wrong band configuration

// Cause 4: Converting between incompatible image types
BufferedImage src = new BufferedImage(100, 100, BufferedImage.TYPE_BYTE_GRAY);
BufferedImage dst = new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB);
Graphics2D g = dst.createGraphics();
g.drawImage(src, 0, 0, null);  // Band mismatch possible
g.dispose();

// Cause 5: Subimage extraction with wrong band specification
BufferedImage src = new BufferedImage(100, 100, BufferedImage.TYPE_INT_RGB);
WritableRaster subRaster = src.getRaster().createWritableChild(
    0, 0, 50, 50, 0, 0, new int[]{0, 1, 2}
);
// May fail if band indices are out of range
```

## Solutions

### Fix 1: Ensure compatible band counts before operations

```java
import java.awt.image.*;

public static boolean areBandsCompatible(BufferedImage img1, BufferedImage img2) {
    int bands1 = img1.getRaster().getNumBands();
    int bands2 = img2.getRaster().getNumBands();
    return bands1 == bands2;
}

public static BufferedImage combineImages(BufferedImage img1, BufferedImage img2) {
    if (!areBandsCompatible(img1, img2)) {
        // Convert to common format
        BufferedImage compatible = new BufferedImage(
            img1.getWidth(), img1.getHeight(), BufferedImage.TYPE_INT_ARGB
        );
        Graphics2D g = compatible.createGraphics();
        g.drawImage(img1, 0, 0, null);
        g.dispose();

        // Now combine
        BufferedImage result = new BufferedImage(
            img1.getWidth(), img1.getHeight(), BufferedImage.TYPE_INT_ARGB
        );
        Graphics2D g2 = result.createGraphics();
        g2.drawImage(compatible, 0, 0, null);
        g2.drawImage(img2, 0, 0, null);
        g2.dispose();
        return result;
    }

    // Bands match — direct combination
    BufferedImage result = new BufferedImage(
        img1.getWidth(), img1.getHeight(), img1.getType()
    );
    Graphics2D g = result.createGraphics();
    g.drawImage(img1, 0, 0, null);
    g.drawImage(img2, 0, 0, null);
    g.dispose();
    return result;
}
```

### Fix 2: Use correct SampleModel for band configuration

```java
import java.awt.image.*;

public static Raster createRasterWithBands(
    int width, int height, int numBands, int dataType
) {
    // Create SampleModel matching band count
    int[] bandOffsets = new int[numBands];
    for (int i = 0; i < numBands; i++) {
        bandOffsets[i] = i;
    }

    int pixelStride = numBands;
    int scanlineStride = width * pixelStride;

    SampleModel model = new PixelInterleavedSampleModel(
        dataType, width, height, pixelStride, scanlineStride, bandOffsets
    );

    int bufferSize = width * height * numBands;
    DataBuffer buffer;
    switch (dataType) {
        case DataBuffer.TYPE_BYTE:
            buffer = new DataBufferByte(new byte[bufferSize], bufferSize);
            break;
        case DataBuffer.TYPE_INT:
            buffer = new DataBufferInt(new int[bufferSize], bufferSize);
            break;
        default:
            throw new IllegalArgumentException("Unsupported data type: " + dataType);
    }

    return Raster.createRaster(model, buffer, null);
}
```

### Fix 3: Validate band structure before writing

```java
import javax.imageio.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public static boolean safeWriteImage(BufferedImage image, File output, String format)
        throws IOException {
    if (image == null) {
        throw new IllegalArgumentException("Image cannot be null");
    }

    int bands = image.getRaster().getNumBands();
    int imageType = image.getType();

    // Validate band configuration for format
    switch (format.toLowerCase()) {
        case "jpg":
            if (bands != 3) {
                // JPEG requires 3 bands — convert to RGB
                BufferedImage rgb = new BufferedImage(
                    image.getWidth(), image.getHeight(), BufferedImage.TYPE_INT_RGB
                );
                Graphics2D g = rgb.createGraphics();
                g.drawImage(image, 0, 0, null);
                g.dispose();
                image = rgb;
            }
            break;
        case "png":
            // PNG supports any band count
            break;
        case "gif":
            // GIF requires indexed color
            if (bands != 1) {
                BufferedImage indexed = new BufferedImage(
                    image.getWidth(), image.getHeight(), BufferedImage.TYPE_BYTE_INDEXED
                );
                Graphics2D g = indexed.createGraphics();
                g.drawImage(image, 0, 0, null);
                g.dispose();
                image = indexed;
            }
            break;
    }

    return ImageIO.write(image, format, output);
}
```

### Fix 4: Handle band extraction safely

```java
import java.awt.image.*;

public static BufferedImage extractBands(
    BufferedImage source, int[] bandsToExtract
) {
    WritableRaster srcRaster = source.getRaster();
    int totalBands = srcRaster.getNumBands();

    // Validate band indices
    for (int band : bandsToExtract) {
        if (band < 0 || band >= totalBands) {
            throw new IllegalArgumentException(
                "Band index " + band + " out of range (0-" + (totalBands - 1) + ")"
            );
        }
    }

    // Create sub-raster with selected bands
    WritableRaster subRaster = srcRaster.createWritableChild(
        0, 0,
        srcRaster.getWidth(), srcRaster.getHeight(),
        0, 0,
        bandsToExtract
    );

    // Create image from sub-raster
    SampleModel sm = subRaster.getSampleModel();
    ColorModel cm = ComponentColorModel.createInstance(
        source.getColorModel().getColorSpace(),
        sm.getDataType(),
        sm.getNumBands(),
        false, false,
        Transparency.TRANSLUCENT
    );

    return new BufferedImage(cm, subRaster, false, null);
}
```

### Fix 5: Convert between image types with band handling

```java
import java.awt.image.*;

public class ImageBandConverter {
    public static BufferedImage convertToRGB(BufferedImage source) {
        if (source.getType() == BufferedImage.TYPE_INT_RGB) {
            return source;
        }

        BufferedImage rgb = new BufferedImage(
            source.getWidth(), source.getHeight(), BufferedImage.TYPE_INT_RGB
        );

        Graphics2D g = rgb.createGraphics();
        g.drawImage(source, 0, 0, null);
        g.dispose();

        return rgb;
    }

    public static BufferedImage convertToARGB(BufferedImage source) {
        if (source.getType() == BufferedImage.TYPE_INT_ARGB) {
            return source;
        }

        BufferedImage argb = new BufferedImage(
            source.getWidth(), source.getHeight(), BufferedImage.TYPE_INT_ARGB
        );

        Graphics2D g = argb.createGraphics();
        g.drawImage(source, 0, 0, null);
        g.dispose();

        return argb;
    }

    public static BufferedImage ensureCompatible(
        BufferedImage source, int targetType
    ) {
        if (source.getType() == targetType) {
            return source;
        }

        BufferedImage converted = new BufferedImage(
            source.getWidth(), source.getHeight(), targetType
        );

        Graphics2D g = converted.createGraphics();
        g.drawImage(source, 0, 0, null);
        g.dispose();

        return converted;
    }
}
```

## Prevention Checklist

- Always verify band count compatibility before combining images.
- Use correct `SampleModel` for the intended band configuration.
- Validate band indices before extracting or manipulating bands.
- Convert images to compatible types before operations.
- Check format-specific band requirements (e.g., JPEG requires 3 bands).
- Handle `IIFImageRankException` when using `ImageIO` writers with mixed sources.

## Related Errors

- [ImagingOpException](../imagingopexception) — image filter operation failure.
- [RasterFormatException](../rasterformatexception) — invalid raster format.
- [IllegalArgumentException](../illegalargumentexception) — invalid band parameters.
