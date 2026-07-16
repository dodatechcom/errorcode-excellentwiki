#!/usr/bin/env python3
"""Split a single sitemap.xml into multiple files (max 49,000 URLs each) and create a sitemap index."""
import os
import sys
import re
from xml.etree import ElementTree as ET

MAX_URLS = 9999

def main():
    sitemap_path = os.path.join("public", "sitemap.xml")
    if not os.path.exists(sitemap_path):
        print("No sitemap.xml found, skipping split.")
        return

    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls = root.findall("sm:url", ns)

    if len(urls) <= MAX_URLS:
        print(f"Sitemap has {len(urls)} URLs, no split needed.")
        return

    print(f"Sitemap has {len(urls)} URLs, splitting into chunks of {MAX_URLS}...")

    # Remove original sitemap.xml (it becomes the index)
    os.remove(sitemap_path)

    # Create individual sitemap files
    sitemap_index_entries = []
    for i in range(0, len(urls), MAX_URLS):
        chunk = urls[i:i + MAX_URLS]
        part_num = (i // MAX_URLS) + 1
        filename = f"sitemap-{part_num}.xml"
        filepath = os.path.join("public", filename)

        part_tree = ET.ElementTree(ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"))
        part_root = part_tree.getroot()
        for url_elem in chunk:
            part_root.append(url_elem)

        ET.indent(part_tree, space="  ")
        part_tree.write(filepath, xml_declaration=True, encoding="UTF-8")
        sitemap_index_entries.append(filename)
        print(f"  Created {filename} with {len(chunk)} URLs")

    # Create sitemap index
    index_root = ET.Element("sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for filename in sitemap_index_entries:
        sitemap_elem = ET.SubElement(index_root, "sitemap")
        loc = ET.SubElement(sitemap_elem, "loc")
        loc.text = f"https://errorcode.excellentwiki.com/{filename}"
        lastmod = ET.SubElement(sitemap_elem, "lastmod")
        from datetime import datetime
        lastmod.text = datetime.now().strftime("%Y-%m-%d")

    index_tree = ET.ElementTree(index_root)
    ET.indent(index_tree, space="  ")
    index_tree.write(sitemap_path, xml_declaration=True, encoding="UTF-8")
    print(f"  Created sitemap.xml index with {len(sitemap_index_entries)} sub-sitemaps")
    print("Done!")

if __name__ == "__main__":
    main()
