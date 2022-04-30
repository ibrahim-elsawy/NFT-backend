import sys
sys.path.append("pixray")
import pixray




def createNft(prompts, quality, aspect_ratio, keyword, init_image, type_image, outDir):
	# prompts = "Squid Game by Hwang Dong-hyuk" #@param {type:"string"} 
	# quality = "draft" #@param ["draft", "normal", "better", "best"] 
	# aspect = "widescreen" #@param ["widescreen", "portrait", "square"] 
	# keyword = []
	# init_image = []
	# typeOfimage = []
	# publich = False
	prompts = prompts + " | " + keyword
	pixray.reset_settings() 
	pixray.add_settings(prompts=prompts, aspect=aspect_ratio, quality=quality, init_image=init_image, ) 
	pixray.add_settings(vector_prompts="textoff", output=outDir) 
	settings = pixray.apply_settings() 
	pixray.do_init(settings) 
	pixray.do_run(settings)


if __name__ == '__main__':
	createNft()
	print("finished............")
