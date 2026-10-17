# 📄 PDF to GitHub Image Workflow

A quick method for embedding PDF pages into GitHub README files, Wikis, Issues, Pull Requests, or Markdown documents without manually converting files to PNG.

## Overview

Instead of exporting PDF pages as images and uploading them separately, use OneNote as an intermediary. GitHub will automatically upload pasted images and generate the required image references.

### Workflow

```text
PDF → Print to OneNote → Ctrl+A → Ctrl+C → Paste into GitHub → Done
```

## Prerequisites

- Microsoft OneNote
- PDF document
- GitHub repository, Wiki, Issue, Pull Request, or Markdown editor

## Steps

### 1. Print the PDF to OneNote

1. Open the PDF.
2. Select **Print**.
3. Choose **Send to OneNote** as the printer.
4. Print the required page(s).

### 2. Copy the Imported Content

1. Open the page in OneNote.
2. Click anywhere on the imported PDF image.
3. Press `Ctrl + A`.
4. Press `Ctrl + C`.

### 3. Paste into GitHub

1. Open your README, Wiki, Issue, or Pull Request.
2. Position the cursor where the image should appear.
3. Press `Ctrl + V`.

GitHub automatically uploads the image and inserts a reference similar to:

```html
<img width="1547" height="11166" alt="image" src="https://github.com/user-attachments/assets/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" />
<br>
```

## Benefits

✅ No PDF-to-PNG conversion required  
✅ No manual image uploads  
✅ High-resolution output  
✅ Fast and simple workflow  
✅ GitHub hosts the image automatically

## Notes

- Images are stored as GitHub attachments rather than repository files.
- For long-term portability, consider storing images within the repository (`docs/images/`) instead.
- Large PDF pages may 