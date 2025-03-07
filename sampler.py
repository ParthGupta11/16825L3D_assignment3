import math
from typing import List

import torch
from ray_utils import RayBundle
from pytorch3d.renderer.cameras import CamerasBase


# Sampler which implements stratified (uniform) point sampling along rays
class StratifiedRaysampler(torch.nn.Module):
    def __init__(self, cfg):
        super().__init__()

        self.n_pts_per_ray = cfg.n_pts_per_ray
        self.min_depth = cfg.min_depth
        self.max_depth = cfg.max_depth

    def forward(
        self,
        ray_bundle,
    ):
        # TODO (Q1.4): Compute z values for self.n_pts_per_ray points uniformly sampled between [near, far]
        # z_vals = self.min_depth + (self.max_depth - self.min_depth) * torch.rand(
        #     self.n_pts_per_ray
        # ).to(ray_bundle.origins.device)
        z_vals = self.min_depth + (self.max_depth - self.min_depth) * torch.linspace(
            0.0, 1.0, self.n_pts_per_ray, device=ray_bundle.origins.device
        )
        z_vals = z_vals.view(-1, 1)

        # TODO (Q1.4): Sample points from z values
        # sample_points = None
        sample_points = []
        for i in range(ray_bundle.origins.shape[0]):
            origs = ray_bundle.origins[i].repeat(self.n_pts_per_ray, 1)
            dirs = ray_bundle.directions[i].repeat(self.n_pts_per_ray, 1)
            pts = origs + (dirs * z_vals)
            sample_points.append(pts)

        sample_points = torch.stack(sample_points, dim=0)

        # Return
        return ray_bundle._replace(
            sample_points=sample_points,
            sample_lengths=z_vals * torch.ones_like(sample_points[..., :1]),
        )


sampler_dict = {"stratified": StratifiedRaysampler}
