# Sama Customer Success/Solutions Engineering Excercise

At Samasource we provide [training data](https://www.samasource.com/blog/2017/12/18/what-is-training-data) for computer vision models.  Whether we're dealing with [image annotation applications](https://www.samasource.com/blog/2018/12/04/training-your-ai-in-3d), metrics to benchmark how well our services are performed, or tools to help integrate customer data pipelines, reporting and working  with images is part of our DNA.  

## Exercise 1  (Architecture & Design)

1.) Write a small program in Python that takes in [an image](https://github.com/Samasource/cse-technical-montreal/blob/main/Question1Images/sample-image.png) and outputs the count of pixels for each unique color in the image in JSON.
   
2.) Render data from the JSON above in a small web page or application. 


## Exercise 2 (Code review and Bug fix)

The python script "Question2.py" is used to identify corrupt images in a folder. But the user reports that the script is running incorrectly, they are not sure what is causing the error. The folder they are running the script on is "Question_2_Images".
Given the python script and 1 sample corrupt image (indexed_5d5da9038aa716043cb777f4_0e2ee618-dab5-48c1-b13f-13ca3f8326e6.png), can you please diagnose what the error(s) are and fix the errors? 


## Clone this repository and share it with abha2.  Please include a README that explains how to clone and run your solution.
1.) On the main page of the repository I clicked on **Code** and cloned using the **Download ZIP** option.
2.) Once I completed the challenge I initialized git by running git init and added all the files while excluding the .idea folder in the .gitignore file.
3.) I then created a new repository on my account and copied the remote repositiory URL and added it as the remote origin by running the following commands
```
git remote add origin https://github.com/otimkpu/cse-technical-montreal-sama.git
git remote -v
git push origin main
```
