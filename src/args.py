#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse


def get_args() -> argparse.Namespace:
    """Get arguments from command line. Default values are used if not specified."""

    parser = argparse.ArgumentParser()

    parser.add_argument("--device", type=int, default=0)
    parser.add_argument("--width", help="cap width", type=int, default=640)
    parser.add_argument("--height", help="cap height", type=int, default=480)

    # parser.add_argument('--upper_body_only', action='store_true')  # 0.8.3 or less
    parser.add_argument(
        "--model_complexity",
        help="model_complexity(0,1(default),2)",
        type=int,
        default=1,
    )
    parser.add_argument(
        "--min_detection_confidence",
        help="min_detection_confidence",
        type=float,
        default=0.5,
    )
    parser.add_argument(
        "--min_tracking_confidence",
        help="min_tracking_confidence",
        type=float,
        default=0.5,
    )
    parser.add_argument("--enable_segmentation", action="store_true")
    parser.add_argument(
        "--segmentation_score_th",
        help="segmentation_score_threshold",
        type=float,
        default=0.5,
    )
    parser.add_argument("--use_brect", action="store_true")
    parser.add_argument("--plot_world_landmark", action="store_true")

    return parser.parse_args()
