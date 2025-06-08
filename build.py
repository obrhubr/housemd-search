import static
import os
import shutil

ASSETS_DIR = "assets"
SITE_DIR = "_site"

def render_pages():
	template = static.read_template(static.TEMPLATE_DIR + "/episode.html")
	data = static.load_data(static.DATA_DIR + "/data.json")

	for s in data.keys():
		for e in data[s].keys():
			episode = data[s][e]

			html = static.render_template(template, episode)

			with open(SITE_DIR + f"/episodes/s{s}e{e}.html", "w") as f:
				f.write(html)

if __name__ == "__main__":
	# Delete all in _site
	shutil.rmtree(SITE_DIR)

	# Create new folders
	os.mkdir(SITE_DIR)
	os.mkdir(SITE_DIR + "/episodes")
	shutil.copytree(ASSETS_DIR, SITE_DIR + "/" + ASSETS_DIR)
	shutil.copyfile(static.DATA_DIR + "/index.json", SITE_DIR + "/" + ASSETS_DIR + "/index.json")
	shutil.copyfile(static.DATA_DIR + "/filters.json", SITE_DIR + "/" + ASSETS_DIR + "/filters.json")

	# Build site
	shutil.copyfile(static.TEMPLATE_DIR + "/index.html", SITE_DIR + "/index.html")
	shutil.copyfile(static.TEMPLATE_DIR + "/about.html", SITE_DIR + "/about.html")
	render_pages()