from pubgis import PUBGIS
import cv2

if __name__ == "__main__":
    match = PUBGIS(full_map_file=r"../full_map_scaled.jpg",
                   mask_file=r"../player_indicator_mask.jpg",
                   debug=True)
    for test_image in [r"bad\squads_dinner_mike_pat_11885.jpg"]:
        mf, coords = match.template_match(cv2.imread(test_image))
        print(coords)
        cv2.waitKey(-1)