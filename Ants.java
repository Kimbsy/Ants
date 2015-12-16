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
  int height = 600;

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

  public static void main(String[] args) {
    new Ants();
  }

  /**
   * Default constructor
   */
  public Ants() {
    super("Life_2.2");
    setSize(900, 600); // 32 is for JFrame top bar
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
    backbuffer = new BufferedImage(width + 200, height, BufferedImage.TYPE_INT_RGB);
    g2d = backbuffer.createGraphics();

    // For mouse input
    addMouseListener(this);

    // For keyboard input
    addKeyListener(this);
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
    g2d.fillRect(900, 0, 0, height);

    // Draw the things.
    printData();
  }

  public void printData() {
    // Set to origin
    g2d.setTransform(identity);

    // Indent
    g2d.translate(15, 10);
    g2d.setColor(new Color(0, 0, 1, 0.5f));
    g2d.setFont(font);

    // Set font
    g2d.setColor(new Color(0, 1, 0.5f, 0.5f));
    g2d.setFont(font);

    // Write framecount to screen
    g2d.translate(0, 30);
    g2d.drawString("frameCount: " + dataNum, 5, 0);
  }

  public void run() {
    // Aquire the current thread
    Thread t = Thread.currentThread();

    // Keep going as long as the thread is alive
    while(t == loop) {
      try {
        // Target framerate is 50fps
        appUpdate();
        Thread.sleep(20);
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

    // @TODO: Do things..

    dataNum++;
    calcFrameRate();
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