import os
import sys
import platform

# Define colors and styles
colors = {
    'folder': '\033[1;32m',    # Bold Green for folders
    'js': '\033[33m',          # Yellow for JavaScript files
    'jsx': '\033[34m',         # Blue for JSX files
    'png': '\033[35m',         # Magenta for PNG files
    'ts': '\033[36m',          # Cyan for TypeScript files
    'md': '\033[31m',          # Red for README.md
    'json': '\033[96m',        # Light Cyan for JSON files
    'cjs': '\033[38;5;208m',   # Orange for CJS files
    'css': '\033[38;5;208m',   # Orange for CSS files
    'svg': '\033[38;5;51m',    # Light Blue for SVG files
    'html': '\033[38;5;75m',   # Light Green for HTML files
    'py': '\033[38;5;226m',    # Yellow for Python files
    'txt': '\033[38;5;244m',   # Grey for TXT files
    'log': '\033[38;5;241m',   # Dark Grey for LOG files
    'default': '\033[0m'       # Reset color
}

def supports_color():
    """
    Check if the terminal supports color.
    """
    plat = sys.platform
    supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ or 'WT_SESSION' in os.environ)
    
    if not supported_platform:
        return False

    if 'COLORTERM' in os.environ:
        return True

    if os.environ.get('TERM') in ['xterm', 'xterm-color', 'xterm-256color', 'linux', 'screen']:
        return True

    return False

def colorize_filename(filename):
    if not supports_color():
        return filename

    if filename == 'README.md':
        color = colors['md']
    elif filename.endswith('.js'):
        color = colors['js']
    elif filename.endswith('.jsx'):
        color = colors['jsx']
    elif filename.endswith('.png'):
        color = colors['png']
    elif filename.endswith('.ts'):
        color = colors['ts']
    elif filename.endswith('.json'):
        color = colors['json']
    elif filename.endswith('.cjs'):
        color = colors['cjs']
    elif filename.endswith('.css'):
        color = colors['css']
    elif filename.endswith('.svg'):
        color = colors['svg']
    elif filename.endswith('.html'):
        color = colors['html']
    elif filename.endswith('.py'):
        color = colors['py']
    elif filename.endswith('.txt'):
        color = colors['txt']
    elif filename.endswith('.log'):
        color = colors['log']
    else:
        color = colors['default']
    return f"{color}{filename}{colors['default']}"

def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')  # Windows
    elif system == 'Linux' or 'ANDROID_ROOT' in os.environ:
        os.system('clear')  # Linux and Termux
    else:
        print("Unsupported OS")

def print_tree(startpath, prefix=''):
    try:
        entries = os.scandir(startpath)
    except PermissionError:
        return

    for entry in entries:
        if entry.is_dir():
            if entry.name not in ('node_modules', 'tree.py', '.git'):
                print(f"{prefix}{colorize_filename(entry.name)}/")
                print_tree(entry.path, prefix + "│   ")
        else:
            print(f"{prefix}{colorize_filename(entry.name)}")

if __name__ == "__main__":
    clear_terminal()  # Clear terminal before printing tree
    startpath = '.'
    if len(sys.argv) > 1:
        startpath = sys.argv[1]
    print_tree(startpath)

