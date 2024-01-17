// Initialize the Earth Engine library
var ee = require('@google/earthengine');

// Load the two TIFF images
var image1 = ee.Image('IMA/Users/splendidsage/Desktop/new/lulc_bengaluru_2016_2.tif');
var image2 = ee.Image('/Users/splendidsage/Desktop/new/lulc_bengaluru_2020_2.tif');

// Compute the absolute difference between corresponding pixels
var diff = image2.subtract(image1).abs();

// Calculate percentage change for each pixel
var percentageChange = diff.divide(image1).multiply(100);

// Display the result
print(percentageChange);

// Visualize the percentage change
var visParams = { min: -100, max: 100, palette: ['red', 'yellow', 'green'] };
Map.addLayer(percentageChange, visParams, 'Percentage Change');
