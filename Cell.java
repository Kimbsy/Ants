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

/**
 * A Cell represents one grid square, it contains information about the pheremone levels inside it.
 */
public class Cell { 

  // The level of pheremones in this cell
  private float pheremoneLevel;

  // Coordinates and size
  private double x, y;
  private double w, h;


  /**
   * Constructor
   */
  public Cell(float initialLevel) {
    this.pheremoneLevel = initialLevel;
  }



  public float getPheremoneLevel() {
    return this.pheremoneLevel;
  }

  public Cell setPheremoneLevel(int pheremoneLevel) {
    this.pheremoneLevel = pheremoneLevel;
    return this;
  }

  public void incPheremoneLevel(float i) {
    float newValue = pheremoneLevel + i;

    if (newValue < 1 && newValue > 0) {
      this.pheremoneLevel += i;
    }
  }

  public double getX() {
    return this.x;
  }

  public Cell setX(double x) {
    this.x = x;
    return this;
  }

  public double getY() {
    return this.y;
  }

  public Cell setY(double y) {
    this.y = y;
    return this;
  }

  public double getW() {
    return this.w;
  }

  public Cell setW(double w) {
    this.w = w;
    return this;
  }

  public double getH() {
    return this.h;
  }

  public Cell setH(double h) {
    this.h = h;
    return this;
  }




  public void draw(Graphics2D g2d) {
    g2d.setColor(new Color(1, 1, 1, this.pheremoneLevel));
    g2d.fillRect((int) this.x, (int) this.y, (int) this.w, (int) this.h);
  }

  public void update() {
    this.incPheremoneLevel(-0.0015f);
  }
}
