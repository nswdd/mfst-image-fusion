
class args():

	# training args
	epochs = 2 #"number of training epochs, default is 2"
	batch_size = 2 #"batch size for training, default is 4"
	dataset_ir = './LLVIP/infrared/train'
	dataset_vi = './LLVIP/visible/train'

	HEIGHT = 256
	WIDTH = 256

	save_fusion_model = "./models/train/transformer_sal21/"
	save_loss_dir = './models/train/transformer_sal21/'

	image_size = 256 #"size of training images, default is 256 X 256"
	cuda = 1 #"set it to 1 for running on GPU, 0 for CPU"
	seed = 42 #"random seed for training"

	lr = 1e-4 #"learning rate, default is 0.001"
	log_interval = 10 #"number of images after which the training loss is logged, default is 500"
	resume_fusion_model = None
	# nest net model
	resume_nestfuse = './models/nestfuse/nestfuse_gray_1e2.model'
	fusion_model = './models/transformer/'



