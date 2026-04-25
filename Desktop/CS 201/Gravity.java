public class Gravity {
    public double falling(double time, double velo){
      return (velo * time + 0.5 * 9.8 * time * time);
    }
  }
