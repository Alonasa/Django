import os
import time
import sass
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class SCSSWatchHandler(FileSystemEventHandler):
    def __init__(self, input_dir, output_dir, main_scss_file):
        self.input_dir = os.path.abspath(input_dir).replace('\\', '/')
        self.output_dir = os.path.abspath(output_dir).replace('\\', '/')
        self.main_scss_file = os.path.abspath(main_scss_file).replace('\\', '/')

    def on_modified(self, event):
        if event.src_path.endswith('.scss'):
            self.compile_scss(self.main_scss_file)

    def compile_scss(self, scss_file):
        try:
            # Normalize scss file path
            scss_file = os.path.normpath(scss_file).replace('\\', '/')
            css_output = os.path.join(self.output_dir, 'style.css').replace('\\', '/')

            # Print debug information
            print(f'Attempting to compile SCSS file:')
            print(f'  SCSS file path: {scss_file}')
            print(f'  CSS output path: {css_output}')

            # Check if SCSS file exists
            if not os.path.isfile(scss_file):
                print(f"Error: {scss_file} does not exist.")
                return

            compiled_css = sass.compile(filename=scss_file)
            with open(css_output, 'w', encoding='utf-8') as css_file:
                css_file.write(compiled_css)
            print(f'Successfully compiled {scss_file} to {css_output}')
        except Exception as e:
            print(f'Error compiling {scss_file}: {e}')


def main():
    # Adjusted the input_dir and output_dir to match the actual file locations
    input_dir = 'A:/DJANGO/portfolio_projects/personal_portfolio/static/sass'
    output_dir = 'A:/DJANGO/portfolio_projects/personal_portfolio/static/css/travel_fellows'
    main_scss_file = os.path.join(input_dir, 'travel_fellows/style.scss')

    # Print the current working directory
    print(f'Current working directory: {os.getcwd()}')

    # Ensure the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: The directory {input_dir} does not exist.")
        return

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    event_handler = SCSSWatchHandler(input_dir, output_dir, main_scss_file)
    observer = Observer()
    observer.schedule(event_handler, path=input_dir, recursive=True)
    observer.start()

    print(f'Watching {input_dir} for changes...')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == '__main__':
    main()