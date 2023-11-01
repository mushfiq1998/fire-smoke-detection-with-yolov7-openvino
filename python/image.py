import yolov7

input = 'data/fire3.jpg'
model = 'fire.xml'
device = 'CPU'
# Enable preprocessing API
pre_api = True
# batchsize = 1
# nireq = 1
grid = None

yolov7_detector = yolov7.FireSmokeDetection(model, device, pre_api, 1, 1, grid)
yolov7_detector.infer_image(input)
