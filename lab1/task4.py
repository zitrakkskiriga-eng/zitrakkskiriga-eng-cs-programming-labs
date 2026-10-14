t_seconds = 7384
hours = t_seconds // 3600
minutes = (t_seconds % 3600) // 60
seconds = t_seconds % 60
print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")