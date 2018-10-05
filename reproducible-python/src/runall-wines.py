import importlib

subset = importlib.import_module('.data.01_subset-data-GBP','src')
plotwines = importlib.import_module('.visualization.02_visualize-wines','src')
county_sub = importlib.import_module('.data.03_country-subset','src')

subset_file = subset.process_data_GBP('data/raw/winemag-data-130k-v2.csv')
plotwines.create_plots(subset_file)
county_sub.get_country(subset_file,'Chile')