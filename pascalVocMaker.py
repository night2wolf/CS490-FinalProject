import xml.etree.ElementTree as ET

def annotationMaker(folder:str, filename:str, path:str, width:int, height: int, name:str, xmin:int, ymin:int, xmax:int, ymax:int, verified:str = "yes", db:str = "Unknown", depth:int = 3, segmented:int = 0, pose:str = "Unspecified", truncated:int = 0, difficult:int = 0):

    ele_annotation = ET.Element("annotation")
    ele_annotation.set("verified", verified)
    

    ele_folder = ET.SubElement(ele_annotation, "folder")
    ele_folder.text = folder
    ele_filename = ET.SubElement(ele_annotation, "filename")
    ele_filename.text = filename
    ele_path = ET.SubElement(ele_annotation, "path")
    ele_path.text = path

    ele_source = ET.SubElement(ele_annotation, "source")
    ele_database = ET.SubElement(ele_source, "database")
    ele_database.text = db

    ele_size = ET.SubElement(ele_annotation, "size")
    ele_width = ET.SubElement(ele_size, "width")
    ele_width.text = str(width)
    ele_height = ET.SubElement(ele_size, "height")
    ele_height.text = str(height)
    ele_depth = ET.SubElement(ele_size, "depth")
    ele_depth.text = str(depth)

    ele_segmented = ET.SubElement(ele_annotation, "segmented")
    ele_segmented.text = str(segmented)

    ele_object = ET.SubElement(ele_annotation, "object")
    ele_name = ET.SubElement(ele_object, "name")
    ele_name.text = name
    ele_pose = ET.SubElement(ele_object, "pose")
    ele_pose.text = pose
    ele_truncated = ET.SubElement(ele_object, "tuncated")
    ele_truncated.text = str(truncated)
    ele_difficult = ET.SubElement(ele_object, "difficult")
    ele_difficult.text = str(difficult)

    ele_bndbox = ET.SubElement(ele_object, "bndbox")
    ele_xmin = ET.SubElement(ele_bndbox, "xmin")
    ele_xmin.text = str(xmin)
    ele_ymin = ET.SubElement(ele_bndbox, "ymin")
    ele_ymin.text = str(ymin)
    ele_xmax = ET.SubElement(ele_bndbox, "xmax")
    ele_xmax.text = str(xmax)
    ele_ymax = ET.SubElement(ele_bndbox, "ymax")
    ele_ymax.text = str(ymax)



    print(ET.dump(ele_annotation))
    tree = ET.ElementTree(ele_annotation)
    out_name = filename[:-3] #remove jpg
    tree.write(out_name + "xml")

if __name__ == "__main__":
    annotationMaker("images", "raccoon-1.jpg", "/Users/datitran/Desktop/raccoon/images/raccoon-1.jpg", 650, 416, "racoon", 81, 88, 522, 408)