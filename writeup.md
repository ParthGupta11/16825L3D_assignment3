# Assignment 3

## A. Neural Volume Rendering 

### 0. Transmittance Calculation

![q0_solution](q0_solution.jpg)

### 1. Differentiable Volume Rendering

#### 1.5. Volume rendering

Volume Rendering Gif

![volume rendering gif](images/part_1.gif)

Depth Visualization using Depth Map

![depth map](depth_map_2.png)

### 2. Optimizing a basic implicit volume

#### 2.3. Visualization

Optimized volume gif

![optimized volume gif](images/part_2.gif)

### 3. Optimizing a Neural Radiance Field (NeRF)

![NeRF Prediction](images/part_3_nerf_without_dir.gif)


### 4. NeRF Extras

#### 4.1 View Dependence

Discuss the trade-offs between increased view dependence and generalization quality -

Results for High Resolution Lego Data
![NeRF Predictions for High Resolution Lego](images/part_3_nerf_w_dir_legohighres.gif)

Results for High Resolution Materials Data
![NeRF Predictions for High Resolution Lego](images/part_3_nerf_w_dir_materialshighres.gif)

## B. Neural Surface Rendering

### 5. Sphere Tracing

![Sphere Tracing](images/part_5.gif)

Writeup describing your implementation - 

For each ray, I initialize a length equal to "self.near" and calculate the points on that ray as the ray_origin + length * ray_direction. Then, for each ray's point, I calculate the values of SDF and then increment the lengths of each ray with their respective length. I repeat this process arbitrary number of times. After the repetition, I calculate the final sdf values for each of the rays. If the sdf values are below the threshold, I mark that as a hit in the mask.

### 6. Optimizing a Neural SDF

| Input GIF | Final GIF|
|-----------|----------|
|![InputGif](images/part_6_input.gif)|![InputGif](images/part_6.gif)|