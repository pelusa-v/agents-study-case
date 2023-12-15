from app.agents.test_agent import test_agent
from app.agents.visor import VisorAgent
from app.utils.image_utils import get_text_from_image

if __name__ == "__main__":
    # test_agent()
    # visor = VisorAgent()
    # visor.query("Read the text in this image please, the local path of the image is: 'app/files/sample.png'")

    get_text_from_image("app/files/sample.png")
