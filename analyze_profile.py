import pstats

stats = pstats.Stats('app_profile')
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats(10)
