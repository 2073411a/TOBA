import java.util.*;

public class Shape{
  public ArrayList<Pixel> pixels;
  public Entity owner;
  public Shape(ArrayList<Pixel> pixels, Entity owner){
    this.owner = owner;
    this.pixels = pixels;
  }
  public Move(long dX, long dY){
    for(Pixel p : pixels){
      p.x += dX;
      p.y += dY;
    }
  }
}
