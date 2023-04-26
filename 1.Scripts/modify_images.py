from PIL import Image
import os

image_folder_location = "C:\\Users\\alvee\\Downloads\\images"
processed_folder_location = r"C:\Users\alvee\OneDrive\Documents\DS Project\RECBuildPlan\Processed_Images"
max_width = 400
max_height = 400
quality = 35

## Reduce Image quality to save space and merge all files from different subfolders contained in the image_folder_location parent folders
##  into one folder.
def image_size_reduce(image_folder_location, output_location, max_width, max_height, quality):
    """
        image_size_reduce reduces the image file sizes and dumps them in a single folder by collecting them from all
            different subfolders of images in image_folder_location.
        image_folder_location is a String representing the location of the main folder that contains all the subfolders of images
        output_location is the String representing the folder location where you want to save all the processed images and must exist
        max_width, max_height and quality are all integers and represents the dimensions and quality of the processed images
    """
    # all subfolders in the folder
    all_subfolders = os.listdir(image_folder_location)
    for i in all_subfolders:
        subfolder_image_location = os.path.join(image_folder_location, i)
        for image_file in os.listdir(subfolder_image_location):
            if image_file.endswith(".jpg"):
            
                # open the image file
                image_path = os.path.join(subfolder_image_location, image_file)
            
                with Image.open(image_path) as image:
                    
                    if image.width > max_width or image.height > max_height:
                        image.thumbnail((max_width, max_height))
            
                # save the images:
                output_path = os.path.join(output_location, image_file)
                image.save(output_path, optimize=True, quality=quality)

    print("Completed!")


if __name__ == "__main__":
    image_size_reduce(image_folder_location, processed_folder_location, max_width, max_height, quality)