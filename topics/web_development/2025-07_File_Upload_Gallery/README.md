# File Upload and Gallery Service

## Problem Statement

Develop a web application where users can upload images and view them in a gallery format. Include basic file validation and a simple gallery display.

## Key Requirements

### Functional Requirements
- **User Interface**: Clean, responsive web interface
- **File Upload**: Click-to-upload functionality
- **File Validation**: Basic image type and file size validation
- **Gallery View**: Simple grid layout displaying uploaded images
- **Image Management**: View and delete individual images
- **Responsive Design**: Works on desktop and mobile

### Technical Requirements
- **Frontend**: Any web framework
- **Backend**: Web server with file handling capabilities
- **File Storage**: Local file system storage
- **Security**: Basic file type validation and size limits

## Detailed Specifications

### File Upload Features
- **Supported Formats**: JPEG, PNG, GIF
- **File Size Limit**: Maximum 5MB per file
- **Upload Methods**: 
  - Click to browse and select files
  - Single file upload (multiple files optional)

### Gallery Features
- **Layout**: Simple responsive grid layout (2-3 columns on desktop, 1 on mobile)
- **Image Display**: Show original images with basic sizing
- **Image Information**: Display file name and upload date
- **Actions**: Delete individual images with confirmation
- **Loading States**: Basic upload progress indicator

### User Experience
- **Visual Feedback**: Success/error messages for uploads
- **Error Handling**: Clear error messages for invalid files
- **Basic Accessibility**: Simple keyboard navigation

## Technical Implementation

### Backend Requirements
```
/api/
├── POST /upload - Upload image file
├── GET /images - Get list of uploaded images
├── DELETE /images/:id - Delete image
└── GET /health - Health check endpoint
```

### File Validation Rules
- **Allowed Extensions**: .jpg, .jpeg, .png, .gif
- **MIME Type Validation**: Basic file type checking
- **Size Validation**: Reject files larger than 5MB

### File Storage
- **Simple Organization**: Store files in a single directory
- **File Naming**: Use timestamp-based naming to avoid conflicts

## Testing Requirements

### Unit Tests
- File validation functions
- API endpoint handlers
- Basic frontend components

### Integration Tests
- Complete upload flow
- Gallery display
- Delete functionality

## Evaluation Criteria
- **Functionality**: Core features work correctly
- **User Experience**: Simple, functional interface
- **Code Quality**: Clean, well-structured code
- **Security**: Basic file validation
- **Testing**: Essential test coverage
- **Docker**: Proper containerization with all dependencies. All tests should run with `docker compose up` command

## Constraints
- **Estimated Time**: 4-8 hours
- **Technology Stack**: No Constraints
- **External Dependencies**: Minimize external libraries
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)

## Bonus Features
- **Drag and Drop Upload**: Enhanced upload experience
- **Multiple File Upload**: Upload several files at once
- **Thumbnail Generation**: Create thumbnails for gallery display
- **Image Dimensions Validation**: Check minimum/maximum image dimensions
- **Advanced File Formats**: Support for WebP format
- **Image Editing**: Basic crop, rotate functionality
- **Album Organization**: Create albums and organize images
- **Sharing**: Generate shareable links for images
- **Search**: Search images by filename
- **Bulk Operations**: Select and delete multiple images
- **Image Compression**: Automatic optimization for web delivery
- **Advanced Gallery**: Lazy loading, pagination, advanced grid layouts
- **Virus Scanning**: Basic file integrity checks
- **Metadata Preservation**: Keep and display original file information 