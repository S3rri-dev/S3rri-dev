// Package the approved bitmap for self-contained SVGs. No creative edits.
import Foundation
import ImageIO
import UniformTypeIdentifiers

let root = URL(fileURLWithPath: #filePath).deletingLastPathComponent().deletingLastPathComponent()
let input = root.appendingPathComponent("assets/avatar.png")
let output = root.appendingPathComponent("assets/avatar-480.png")
guard let source = CGImageSourceCreateWithURL(input as CFURL, nil),
      let image = CGImageSourceCreateThumbnailAtIndex(source, 0, [
        kCGImageSourceCreateThumbnailFromImageAlways: true,
        kCGImageSourceThumbnailMaxPixelSize: 480,
        kCGImageSourceCreateThumbnailWithTransform: true
      ] as CFDictionary),
      let destination = CGImageDestinationCreateWithURL(output as CFURL, UTType.png.identifier as CFString, 1, nil)
else { fatalError("Cannot prepare avatar thumbnail") }
CGImageDestinationAddImage(destination, image, nil)
guard CGImageDestinationFinalize(destination) else { fatalError("Cannot save avatar thumbnail") }
print("Prepared avatar-480.png: \(image.width) × \(image.height)")
