import AppKit
import Foundation

// Tarjetas originales de composición vectorial; no modifica el avatar ni capturas.
let destination = URL(fileURLWithPath: CommandLine.arguments.count > 1 ? CommandLine.arguments[1] : "assets", isDirectory: true)
try FileManager.default.createDirectory(at: destination, withIntermediateDirectories: true)
func color(_ hex: UInt32) -> NSColor {
    NSColor(srgbRed: CGFloat((hex >> 16) & 255)/255, green: CGFloat((hex >> 8) & 255)/255, blue: CGFloat(hex & 255)/255, alpha: 1)
}
func block(_ x: CGFloat, _ y: CGFloat, _ w: CGFloat, _ h: CGFloat, _ fill: UInt32) {
    color(fill).setFill()
    NSBezierPath(rect: NSRect(x: x, y: 640-y-h, width: w, height: h)).fill()
}
func text(_ value: String, _ x: CGFloat, _ y: CGFloat, _ size: CGFloat, _ fill: UInt32, bold: Bool = false, width: CGFloat = 1120) {
    let attributes: [NSAttributedString.Key: Any] = [
        .font: NSFont.systemFont(ofSize: size, weight: bold ? .bold : .regular),
        .foregroundColor: color(fill)
    ]
    NSAttributedString(string: value, attributes: attributes).draw(in: NSRect(x: x, y: 640-y-size*1.5, width: width, height: size*1.5))
}
let cards: [(file: String, title: String, subtitle: String, detail: String, index: String)] = [
    ("social-profile", "S3rri.dev", "Desarrollo de software y sistemas.", "PROYECTOS / DECISIONES / VERIFICACIÓN", "DEV"),
    ("social-nodal", "Nodal", "Calendario, estudio y notas. En tu Mac.", "SWIFT / APPKIT / WEBKIT / SQLITE", "01"),
    ("social-caudal", "Caudal", "Tu dinero, con perspectiva. En tu Mac.", "SWIFT / APPKIT / WEBKIT / SQLITE", "02"),
    ("social-umbral", "Umbral", "Tu catálogo de utilidades en la barra de menús.", "SWIFTUI / APPKIT / APPLE SILICON", "03")
]
for card in cards {
    let bitmap = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: 1280, pixelsHigh: 640, bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
    NSGraphicsContext.saveGraphicsState()
    NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: bitmap)
    block(0, 0, 1280, 640, 0x000000)
    block(0, 0, 16, 640, 0x8B1722)
    block(72, 100, 1136, 2, 0x302428)
    text("S3RRI.DEV", 72, 43, 24, 0xC5A05A, bold: true)
    text("SOFTWARE / SISTEMAS", 848, 47, 17, 0xC7C1BE, width: 360)
    text(card.index, 965, 144, 126, 0x261013, bold: true, width: 300)
    text(card.title, 64, 170, 112, 0xF7F3ED, bold: true, width: 900)
    text(card.subtitle, 72, 337, 31, 0xF7F3ED)
    block(72, 434, 88, 5, 0x8B1722)
    text(card.detail, 72, 466, 22, 0xC5A05A, bold: true)
    block(72, 560, 1136, 2, 0x302428)
    text("Código abierto para revisar. Proyectos personales.", 72, 582, 18, 0xC7C1BE)
    NSGraphicsContext.restoreGraphicsState()
    let png = bitmap.representation(using: .png, properties: [:])!
    try png.write(to: destination.appendingPathComponent(card.file + ".png"))
    print("\(card.file).png · 1280×640 · \(png.count) bytes")
}
