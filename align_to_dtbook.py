import json
import xml.etree.ElementTree as ET
from datetime import date

# Đọc file JSON
with open("./alignResult/aligned_result_corrected.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# ==== Tạo cấu trúc DTBook ====
NS = "http://www.daisy.org/z3986/2005/dtbook/"
ET.register_namespace('', NS)

dtbook = ET.Element("{%s}dtbook" % NS, {
    "xml:lang": "vi-VN",
    "version": "2005-3"
})

# ---- HEAD ----
head = ET.SubElement(dtbook, "head")
meta_info = {
    "dtb:uid": "AUTO-UID-7016948210013975649-packaged",
    "dtb:generator": "JSON-to-DTBook Python Script",
    "dc:Title": "Hoi70",
    "dc:Creator": "Thi Nai Am",
    "dc:Date": str(date.today()),
    "dc:Publisher": "NXB Van Hoc",
    "dc:Identifier": "AUTO-UID-7016948210013975649-packaged",
    "dc:Language": "vi-VN",
}
for k, v in meta_info.items():
    ET.SubElement(head, "meta", {"name": k, "content": v})

# ---- BOOK ----
book = ET.SubElement(dtbook, "book", {"showin": "blp"})

# ---- FRONTMATTER ----
frontmatter = ET.SubElement(book, "frontmatter")

doctitle = ET.SubElement(frontmatter, "doctitle", {"id": "forsmil-1", "smilref": "mo0.smil#sforsmil-1"})
ET.SubElement(doctitle, "sent", {"id": "id_1", "smilref": "mo0.smil#sid_1"}).text = "Hồi 70"

docauthor = ET.SubElement(frontmatter, "docauthor", {"id": "forsmil-2", "smilref": "mo0.smil#sforsmil-2"})
ET.SubElement(docauthor, "sent", {"id": "id_2", "smilref": "mo0.smil#sid_2"}).text = "Thi Nai Am"

# ---- BODYMATTER ----
bodymatter = ET.SubElement(book, "bodymatter", {"id": "bodymatter_0001"})
level1 = ET.SubElement(bodymatter, "level1")

h1 = ET.SubElement(level1, "h1", {"id": "faux-heading", "smilref": "mo0.smil#sfaux-heading"})
ET.SubElement(h1, "sent", {"id": "id_3", "smilref": "mo0.smil#sid_3"}).text = "Section"

# ---- ADD PARAGRAPHS FROM JSON ----
sent_id_counter = 4
para_counter = 1
for seg in data["segments"]:
    p = ET.SubElement(level1, "p", {"id": f"hoi70_{para_counter}",
    "smilref": f"mo0.smil#seq_{para_counter}"})
    ET.SubElement(p, "sent", {
        "id": f"id_{sent_id_counter}",
        "smilref": f"mo0.smil#sid_{sent_id_counter}"
    }).text = seg["text"]
    sent_id_counter += 1
    para_counter += 1

xml_str = ET.tostring(dtbook, encoding="utf-8", xml_declaration=False)

with open("./output/hoi70/dtbook.xml", "wb") as f:
    f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
    f.write(b'<!DOCTYPE dtbook PUBLIC "-//NISO//DTD dtbook 2005-3//EN" "http://www.daisy.org/z3986/2005/dtbook-2005-3.dtd">\n')
    f.write(xml_str)

print("✅ Đã tạo file ./output/hoi70/dtbook.xml thành công!")
