# File Upload and Gallery Service

## Problem Statement
Develop a web application where users can upload images, view them in a gallery format, and delete their uploads. Include basic file validation and thumbnail generation.

## Key Requirements

### Functional Requirements
- **User Interface**: Clean, responsive web interface
- **File Upload**: Drag-and-drop or click-to-upload functionality
- **File Validation**: Validate image types, file sizes, and dimensions
- **Gallery View**: Grid layout displaying uploaded images
- **Thumbnail Generation**: Create thumbnails for gallery display
- **Image Management**: View, delete individual images
- **Responsive Design**: Works on desktop, tablet, and mobile

### Technical Requirements
- **Frontend**: Modern web framework (React, Vue, Angular, or vanilla JS)
- **Backend**: Web server with file handling capabilities
- **File Storage**: Local file system or database storage
- **Image Processing**: Thumbnail generation and image optimization
- **Security**: File type validation, size limits, secure file handling

## Detailed Specifications

### File Upload Features
- **Supported Formats**: JPEG, PNG, GIF, WebP
- **File Size Limit**: Maximum 10MB per file
- **Image Dimensions**: Minimum 100x100 pixels, maximum 4000x4000 pixels
- **Upload Methods**: 
  - Drag and drop from file explorer
  - Click to browse and select files
  - Multiple file selection support

### Gallery Features
- **Layout**: Responsive grid layout (3-5 columns on desktop, 2-3 on tablet, 1 on mobile)
- **Thumbnails**: 200x200 pixel thumbnails with aspect ratio preservation
- **Image Information**: Display file name, upload date, file size
- **Actions**: Delete individual images with confirmation
- **Loading States**: Show upload progress and loading indicators

### User Experience
- **Visual Feedback**: Progress bars for uploads, success/error messages
- **Error Handling**: Clear error messages for invalid files
- **Accessibility**: Keyboard navigation, screen reader support
- **Performance**: Lazy loading for large galleries, optimized image delivery

## Technical Implementation

### Backend Requirements
```
/api/
├── POST /upload - Upload image file
├── GET /images - Get list of uploaded images
├── GET /images/:id - Get specific image details
├── GET /images/:id/thumbnail - Get thumbnail
├── DELETE /images/:id - Delete image
└── GET /health - Health check endpoint
```

### Frontend Structure
```
src/
├── components/
│   ├── FileUpload.js
│   ├── ImageGallery.js
│   ├── ImageCard.js
│   └── UploadProgress.js
├── services/
│   ├── api.js
│   └── imageProcessor.js
├── styles/
│   ├── main.css
│   └── responsive.css
└── utils/
    ├── validation.js
    └── helpers.js
```

### File Validation Rules
- **Allowed Extensions**: .jpg, .jpeg, .png, .gif, .webp
- **MIME Type Validation**: Check actual file content, not just extension
- **Size Validation**: Reject files larger than 10MB
- **Dimension Validation**: Use image metadata to check dimensions
- **Virus Scanning**: Basic file integrity checks (optional)

### Image Processing
- **Thumbnail Generation**: Create 200x200 thumbnails
- **Format Optimization**: Convert to WebP for better compression
- **Metadata Preservation**: Keep original file information
- **Storage Organization**: Organize files by date/user

## Example API Responses

### Upload Response
```json
{
  "success": true,
  "image": {
    "id": "uuid-123",
    "filename": "vacation.jpg",
    "originalName": "vacation_photo.jpg",
    "size": 2048576,
    "width": 1920,
    "height": 1080,
    "uploadDate": "2025-07-01T10:30:00Z",
    "thumbnailUrl": "/api/images/uuid-123/thumbnail"
  }
}
```

### Gallery Response
```json
{
  "images": [
    {
      "id": "uuid-123",
      "filename": "vacation.jpg",
      "size": 2048576,
      "width": 1920,
      "height": 1080,
      "uploadDate": "2025-07-01T10:30:00Z",
      "thumbnailUrl": "/api/images/uuid-123/thumbnail"
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 20
}
```

## Testing Requirements

### Unit Tests
- File validation functions
- Image processing utilities
- API endpoint handlers
- Frontend components

### Integration Tests
- Complete upload flow
- Gallery display and pagination
- Delete functionality
- Error handling scenarios

### End-to-End Tests
- User uploads multiple files
- User deletes images
- Responsive design testing
- Cross-browser compatibility

## Evaluation Criteria
- **Functionality**: All features work correctly
- **User Experience**: Intuitive, responsive interface
- **Code Quality**: Clean, well-structured, documented code
- **Security**: Proper file validation and secure handling
- **Performance**: Fast uploads and gallery loading
- **Testing**: Comprehensive test coverage
- **Docker**: Proper containerization with all dependencies

## Constraints
- **Estimated Time**: 6-8 hours
- **Technology Stack**: Any modern web technologies
- **External Dependencies**: Minimize external libraries
- **Browser Support**: Modern browsers (Chrome, Firefox, Safari, Edge)

## Bonus Features
- **Image Editing**: Basic crop, rotate, filter functionality
- **Album Organization**: Create albums and organize images
- **Sharing**: Generate shareable links for images
- **Search**: Search images by filename or tags
- **Bulk Operations**: Select and delete multiple images
- **Image Compression**: Automatic optimization for web delivery 