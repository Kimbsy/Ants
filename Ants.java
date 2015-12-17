/***************************************************************************
* Copyright 2016 Dave Kimber
* 
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
* 
*     http:// Www.apache.org/licenses/LICENSE-2.0
* 
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
***************************************************************************/

import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import java.awt.image.*;
import java.util.*;
import java.util.ArrayList;
import java.util.List;
import javax.swing.*;

// Primary game class
public class Ants extends JFrame implements Runnable, MouseListener, KeyListener {

  // Main thread becomes the app loop
  Thread loop;

  // Back buffer
  BufferedImage backbuffer;

  // Main drawing object for backbuffer
  Graphics2D g2d;

  // Width/height of frame
  int width = 900;
  int height = 900;

  // Size of grid
  int gridSize = 100;

  // Create identity transform
  AffineTransform identity = new AffineTransform();

  // Create random number generator
  Random rand = new Random();

  // Number of frames past
  int dataNum = 0;

  // MouseListener variables
  int clickX;
  int clickY;
  int mouseButton;

  // Font for displaying data
  Font font = new Font("Courier", Font.PLAIN, 12);

  // Frame rate counters and other timing variables
  int frameCount = 0, frameRate = 0;
  long startTime = System.currentTimeMillis();

  // Cell ArrayList
  List<Cell> cells = Collections.synchronizedList(new ArrayList<Cell>());

  public static void main(String[] args) {
    new Ants();
  }

  /**
   * Default constructor
   */
  public Ants() {
    super("Life_2.2");
    setSize(width, height); // 32 is for JFrame top bar
    setVisible(true);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

    loop = new Thread(this);
    loop.start();
    init();
  }

  /**
   * Application init event
   */
  public void init() {
    // Create the backbuffer for smooth-ass graphics
    backbuffer = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
    g2d = backbuffer.createGraphics();

    // For mouse input
    addMouseListener(this);

    // For keyboard input
    addKeyListener(this);

    // Create cells
    initCells();
  }

  public void initCells() {
    for (int i = 0; i < gridSize; i++) {
      for (int j = 0; j < gridSize; j++) {
        double w = (width / gridSize);
        double h = (height / gridSize);
        double x = w * i;
        double y = h * j;
        float initialLevel = rand.nextFloat();
        Cell c = new Cell(initialLevel);
        c.setX(x);
        c.setY(y);
        c.setW(w);
        c.setH(h);
        cells.add(c);
      }
    }
  }

  /**
   * Paint event draws to the screen.
   * 
   * @param java.awt.Graphics g
   *   Graphics object.
   */
  public void paint(Graphics g) {
    // Draw the backbuffer to the window
    g.drawImage(backbuffer, 0, 0, this);

    // Start off transforms at identity
    g2d.setTransform(identity);

    // Erase the background
    g2d.setColor(Color.BLACK);
    g2d.fillRect(0, 0, width, height);
    g2d.setColor(Color.WHITE);
    g2d.fillRect(width, 0, 0, height);

    // Draw the things.
    drawGrid();
    drawData();
  }

  /**
   * Draw the grid of cells to the screen, then get each cell to draw itself.
   */
  public void drawGrid() {
    // Set to origin
    g2d.setTransform(identity);

    // Set color
    g2d.setColor(new Color(0, 0, 1, 0.5f));

    // Draw horizontal lines
    for (int i = 0; i < gridSize; i++) {
      double y = (height / gridSize) * i;
      g2d.draw(new Line2D.Double(0, y, width, y));
    }

    // Draw vertical lines
    for (int i = 0; i < gridSize; i++) {
      double x = (width / gridSize) * i;
      g2d.draw(new Line2D.Double(x, 0, x, height));
    }

    // Draw cells
    synchronized (cells) {
      Iterator<Cell> cellIterator = cells.iterator();
      while (cellIterator.hasNext()) {
        Cell c = (Cell) cellIterator.next();
        c.draw(g2d);
      }
    }

  }

  /**
   * Print information to the screen
   */
  public void drawData() {
    // Set to origin
    g2d.setTransform(identity);

    // Indent
    g2d.translate(15, 10);

    // Set font
    g2d.setColor(new Color(0, 1, 0.5f, 0.5f));
    g2d.setFont(font);

    // Write framecount to screen
    g2d.translate(0, 30);
    g2d.drawString("frameRate: " + frameRate, 5, 0);
  }

  public void run() {
    // Aquire the current thread
    Thread t = Thread.currentThread();

    // Keep going as long as the thread is alive
    while(t == loop) {
      try {
        // Target framerate is 100fps
        appUpdate();
        Thread.sleep(10);
      } catch(InterruptedException e) {
        e.printStackTrace();
      }
      repaint();
    }
  }

  /**
   * Stop thread event.
   */
  public void stop() {
    // Kill the loop thread
    loop = null;
  }

  /**
   * Move and animate objects in the app.
   */
  public void appUpdate() {
    updateCells();

    dataNum++;
    calcFrameRate();
  }

  public void updateCells() {
    synchronized (cells) {
      Iterator<Cell> cellIterator = cells.iterator();
      while (cellIterator.hasNext()) {
        Cell c = (Cell) cellIterator.next();
        c.update();
      }
    }
  }

  public void calcFrameRate() {
    // Calculate frame rate
    frameCount++;
    if(System.currentTimeMillis() > startTime+1000) {
      startTime  = System.currentTimeMillis();
      frameRate  = frameCount;
      frameCount = 0;
    }
  }

  /**
   * MouseListener click method.
   * 
   * @param java.awt.event.MouseEvent e
   *   The mouse event.
   */
  public void mouseClicked(MouseEvent e) {
    clickX = e.getX();
    clickY = e.getY();
    checkButton(e);
  }

  public void mousePressed(MouseEvent e) { }

  public void mouseReleased(MouseEvent e) { }

  public void mouseExited(MouseEvent e) { }

  public void mouseEntered(MouseEvent e) { }

  /**
   * Custom method to get mouse button status.
   * 
   * @param java.awt.event.MouseEvent e
   *   The mouse event.
   */
  public void checkButton(MouseEvent e) {
    switch(e.getButton()) {
      case MouseEvent.BUTTON1:
        mouseButton = 1;
        break;
      case MouseEvent.BUTTON2:
        mouseButton = 2;
        break;
      case MouseEvent.BUTTON3:
        mouseButton = 3;
        break;
      default:
        mouseButton = 0;
    }
  }

  public void keyPressed(KeyEvent k) {
    int keycode = k.getKeyCode();
  }

  public void keyReleased(KeyEvent k) {
    int keycode = k.getKeyCode();
  }

  public void keyTyped(KeyEvent k) { }
}