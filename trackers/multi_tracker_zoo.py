from trackers.strongsort.utils.parser import get_config


def create_tracker(tracker_type, tracker_config, reid_weights, device, half):
    
    cfg = get_config()
    cfg.merge_from_file(tracker_config)
    
    if tracker_type == 'strongsort':
        from trackers.strongsort.strong_sort import StrongSORT
        strongsort = StrongSORT(
            reid_weights,
            device,
            half,
            max_dist=cfg.strongsort.max_dist,
            max_iou_dist=cfg.strongsort.max_iou_dist,
            max_age=cfg.strongsort.max_age,
            max_unmatched_preds=cfg.strongsort.max_unmatched_preds,
            n_init=cfg.strongsort.n_init,
            nn_budget=cfg.strongsort.nn_budget,
            mc_lambda=cfg.strongsort.mc_lambda,
            ema_alpha=cfg.strongsort.ema_alpha,

        )
        return strongsort
    
    elif tracker_type == 'ocsort':
        from trackers.ocsort.ocsort import OCSort
        ocsort = OCSort(
            det_thresh=cfg.ocsort.det_thresh,
            max_age=cfg.ocsort.max_age,
            min_hits=cfg.ocsort.min_hits,
            iou_threshold=cfg.ocsort.iou_thresh,
            delta_t=cfg.ocsort.delta_t,
            asso_func=cfg.ocsort.asso_func,
            inertia=cfg.ocsort.inertia,
            use_byte=cfg.ocsort.use_byte,
        )
        return ocsort
    
    elif tracker_type == 'bytetrack':
        from trackers.bytetrack.byte_tracker import BYTETracker
        bytetracker = BYTETracker(
            track_thresh=cfg.bytetrack.track_thresh,
            match_thresh=cfg.bytetrack.match_thresh,
            track_buffer=cfg.bytetrack.track_buffer,
            frame_rate=cfg.bytetrack.frame_rate
        )
        return bytetracker
    elif tracker_type == 'strong_ocsort':
        from trackers.strong_ocsort.strong_ocsort import StrongOCSort
        # initialize Strong-OCSort
        cfg = get_config()
        cfg.merge_from_file('trackers/strong_ocsort/configs/strong_ocsort.yaml')

        strongocsort = StrongOCSort(
            reid_weights,
            device,
            half,
            det_thresh=cfg.strong_ocsort.det_thresh,
            max_dist=cfg.strong_ocsort.max_dist,
            nn_budget=cfg.strong_ocsort.nn_budget,
            ema_alpha=cfg.strong_ocsort.ema_alpha,
            max_age=cfg.strong_ocsort.max_age,
            min_hits=cfg.strong_ocsort.min_hits,
            iou_threshold=cfg.strong_ocsort.iou_treshold,
            delta_t=cfg.strong_ocsort.delta_t,
            inertia=cfg.strong_ocsort.inertia,
            use_byte=cfg.strong_ocsort.use_byte,
            use_resurrection=cfg.strong_ocsort.use_resurrection,
        )

        return strongocsort
    else:
        print('No such tracker')
        exit()