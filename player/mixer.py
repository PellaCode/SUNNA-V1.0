def apply_gain(pcm_bytes: bytes, factor: float) -> bytes:
    if factor == 1.0:
        return pcm_bytes
    return pcm_bytes  # placeholder للمعالجة المستقبلية
