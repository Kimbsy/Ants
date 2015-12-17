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
  float pheremoneLevel;


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

  public void incPheremoneLevel(int i) {
    this.pheremoneLevel += i;
  }



  public void draw(Graphics2D g2d, double x, double y, double w, double h) {
    float intensity = this.pheremoneLevel;

    g2d.setColor(new Color(1, 1, 1, intensity));
    g2d.fillRect((int) x, (int) y, (int) w, (int) h);
  }
}
