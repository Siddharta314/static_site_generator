# Static Site Generator

A simple, custom-built Static Site Generator (SSG) written in Python. This project transforms Markdown files into a full HTML website using a recursive processing engine and a custom HTML node system.

## Features

- **Markdown to HTML**: Converts headers, bold text, italics, code blocks, links, and images.
- **Recursive Generation**: Automatically mirrors your `content/` directory structure into the `public/` folder.
- **Static Asset Management**: Synchronizes your CSS and images from a `static/` directory.
- **Custom HTML Engine**: Uses a bespoke internal representation of HTML nodes (LeafNodes and ParentNodes).
- **Template System**: Simple `{{ Title }}` and `{{ Content }}` injection.

## Project Structure

- `src/`: Python source code.
    - `models/`: Class definitions for HTML and Text nodes.
    - `processing/`: Logic for parsing Markdown and splitting nodes.
- `static/`: Raw assets (CSS, images).
- `content/`: Your website content written in Markdown.
- `public/`: The generated production-ready HTML site.
- `template.html`: The base HTML structure for your pages.

## Getting Started

### Prerequisites

- Python 3.10 or higher.

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/youruser/static-site-generator.git](https://github.com/youruser/static-site-generator.git)
   cd static-site-generator
