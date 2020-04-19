import xml.etree.ElementTree as ET
import os
import shutil


def annotation_maker(folder: str, filename: str, path: str, width: int, height: int, name: str, xmin: int, ymin: int,
                     xmax: int, ymax: int, verified: str = "yes", db: str = "Unknown", depth: int = 3,
                     segmented: int = 0, pose: str = "Unspecified", truncated: int = 0, difficult: int = 0,
                     out_dir_path=".", file_extension="JPEG"):
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

    tree = ET.ElementTree(ele_annotation)

    extension_length = len(file_extension)
    out_name = filename[:-extension_length]  # remove jpeg
    out_name += "xml"
    out_path = os.path.join(out_dir_path, out_name)
    tree.write(out_path)


def dir_to_pascal_voc(dir_path: str, out_path: str):
    class_folders = os.listdir(dir_path)
    print(class_folders)

    for class_folder in class_folders:
        class_folder_path = os.path.join(dir_path, class_folder)

        class_folder_dest = os.path.join(out_path, class_folder)
        if not os.path.exists(class_folder_dest):
            os.mkdir(class_folder_dest)

        annotations_dest = os.path.join(class_folder_dest, "annotations")
        if not os.path.exists(annotations_dest):
            os.mkdir(annotations_dest)

        images_dest = os.path.join(class_folder_dest, "images")
        if not os.path.exists(images_dest):
            os.mkdir(images_dest)

        bb_text = os.path.join(class_folder_path, class_folder + "_boxes.txt")

        fh = open(bb_text)
        bounding_boxes = fh.readlines()
        fh.close()

        bounding_boxes = [line.split() for line in bounding_boxes]

        images_path = os.path.join(class_folder_path, "images")
        images = os.listdir(images_path)

        for image in images:

            image_path = os.path.join(images_path, image)
            image_dest = os.path.join(images_dest, image)

            underscore_idx = image.find("_")
            dot_idx = image.find(".")
            image_idx = int(image[underscore_idx + 1:dot_idx])

            image_bb = bounding_boxes[image_idx]
            x_min, y_min, x_max, y_max = image_bb[1:]

            if not os.path.exists(image_dest):
                shutil.copy(image_path, image_dest)

            annotation_maker("images", image, image_dest, 64, 64, class_folder, x_min, y_min, x_max, y_max,
                             out_dir_path=annotations_dest)


if __name__ == "__main__":

    # annotationMaker("images", "raccoon-1.jpg", "/Users/datitran/Desktop/raccoon/images/raccoon-1.jpg", 650, 416,
    #                 "racoon", 81, 88, 522, 408)

    train_dir = os.path.join("tiny-imagenet-200", "train")

    new_dataset_root_name = "dataset"
    if not os.path.exists(new_dataset_root_name):
        os.mkdir(new_dataset_root_name)

    new_train_dir_name = "train"
    new_train_dir = os.path.join(new_dataset_root_name, new_train_dir_name)
    if not os.path.exists(new_train_dir):
        os.mkdir(new_train_dir)

    dir_to_pascal_voc(train_dir, new_train_dir)
