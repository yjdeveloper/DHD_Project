1. Clone "DHD_Project" repository from the GitHub
2. Navigate to local disk D using the cmd and change directory to "DHD_Project".
3. Use the following command to activate the environment:
                    
                    Scripts\activate

4. Now change the directory to "Project".
5. All the scanned images are stored in "Dataset" folder.
6. How to threshold/binarized the images in bulk?

                python bulk_thresholding.py

7. The binarized images are all stored in "Thresholded" folder. 
8. How to fill the pixels (dilation) to the broken images?

                python morphological_operations.py

9. The dilated images are all stored in "Dilated" folder.
10. How to automatically crop the digits?

                python automatic_cropping.py --image Dilated/Sheet_1.jpg

11. The cropped images are all stored in "Cropped" directory.
12. How to removed unwanted noise from the cropped image?

                python remove_small_blobs.py
