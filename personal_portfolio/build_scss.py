import os
import time
import sass
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class SCSSWatchHandler(FileSystemEventHandler):
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir

    def on_modified(self, event):
        if event.src_path.endswith('.scss'):
            self.compile_scss(event.src_path)

    def compile_scss(self, scss_file):
        try:
            css_output = os.path.join(self.output_dir, 'style.css')
            print(f'Compiling {scss_file} to {css_output}')
            compiled_css = sass.compile(filename=scss_file)
            with open(css_output, 'w', encoding='utf-8') as css_file:
                css_file.write(compiled_css)
            print(f'Successfully compiled {scss_file} to {css_output}')
        except Exception as e:
            print(f'Error compiling {scss_file}: {e}')


def main():
    input_dir = 'static/sass'
    output_dir = 'static/css/travel_fellows'

    # Ensure the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: The directory {input_dir} does not exist.")
        return

    # Ensure the output directory exists
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    event_handler = SCSSWatchHandler(input_dir, output_dir)
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
