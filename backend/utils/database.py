import os
import pathlib
from typing import Dict, List
from .checker import *


class ClothesDatabase:
    db_attributes: List[str] = ["cloth_color", "cloth_size"]
    clothes_db: List[str] = []

    def __init__(self, image_folder: str) -> None:
        check_folder_exist(image_folder)
        for file_ in os.listdir(image_folder):
            image_path = os.path.join(image_folder, file_)
            check_file_exist(image_path)
            self.clothes_db.append(image_path)

    def retrieve_like_clothes(self, cloth_attributes: Dict) -> str:
        (
            find_,
            total_high_score,
            total_high_index,
            match_high_score,
            match_high_index,
        ) = (
            False,
            0,
            -1,
            0,
            -1,
        )

        for f_idx, file_ in enumerate(self.clothes_db):
            basename = pathlib.Path(file_).stem
            _, cloth_color, cloth_size, score = basename.split("_")
            cur_cloth_attribute_dict = {
                "cloth_color": cloth_color,
                "cloth_size": cloth_size,
                "score": float(score),
            }

            match_ = True
            for db_attribute in self.db_attributes:
                if (
                    cur_cloth_attribute_dict[db_attribute]
                    != cloth_attributes[db_attribute]
                ):
                    match_ = False

            if match_:
                find_ = True
                if cur_cloth_attribute_dict["score"] > match_high_score:
                    match_high_score = cur_cloth_attribute_dict["score"]
                    match_high_index = f_idx

            if cur_cloth_attribute_dict["score"] > total_high_score:
                total_high_score = cur_cloth_attribute_dict["score"]
                total_high_index = f_idx

        if find_:
            return self.clothes_db[match_high_index], match_high_score
        else:
            return self.clothes_db[total_high_index], total_high_score
