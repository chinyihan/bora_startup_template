import subprocess
import yaml
import os

# Function to create/update YAML file with curly brackets
def create_yaml_file(file_path):
    with open(file_path, 'w') as file:
        file.write("{}")

# Load current settings from settings.yaml
with open('settings.yaml', 'r') as file:
    current_settings = yaml.safe_load(file)

# Ask user for new title and port
new_title = input("Enter the new title: ")
new_port = input("Enter the new port: ")

# Update settings
current_settings['title'] = new_title
current_settings['port'] = new_port

# Write back to settings.yaml
with open('settings.yaml', 'w') as file:
    yaml.dump(current_settings, file)

print("Settings updated successfully!")

# Clone the latest version of Bora repository
bora_repo_url = "https://github.com/kit-ipe/bora.git"
bora_clone_path = "bora"  # This assumes 'bora' is the desired destination folder
subprocess.run(['git', 'clone', bora_repo_url, bora_clone_path])

# Create or update style.yaml and varname.yaml with curly brackets in 'mytest' directory
create_yaml_file(os.path.join('mytest', 'style.yaml'))
create_yaml_file(os.path.join('mytest', 'varname.yaml'))

# Change to the 'bora' directory
os.chdir(bora_clone_path)

# Add a default background image to style.yaml in 'mytest' directory
default_background_image_path = "default_background.jpg"
with open(os.path.join('mytest', 'style.yaml'), 'w') as style_file:
    yaml.dump({'background_image': default_background_image_path}, style_file)

# Ask user for their background image path
user_background_image_path = input("Enter the path to your background image (or press Enter to use the default): ")
background_image_path = user_background_image_path if user_background_image_path else default_background_image_path

if os.path.isfile(background_image_path):
    with open(os.path.join('mytest', 'style.yaml'), 'r') as style_file:
        style_data = yaml.safe_load(style_file)

    style_data['background_image'] = background_image_path

    with open(os.path.join('mytest', 'style.yaml'), 'w') as style_file:
        yaml.dump(style_data, style_file)

    print("Background image added to style.yaml.")
else:
    print("Invalid image path. Make sure the file exists.")
