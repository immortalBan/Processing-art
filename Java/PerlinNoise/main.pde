float speed = 40;
int amount = 20000;
float l = 0.005;
ArrayList<Particle> particles = new ArrayList(0);

void setup() {
  fullScreen();
  colorMode(HSB);
  background(0);
  for (int i = 0; i < width; i+=20) {
    for (int j = 0; j < height; j+=20) {
      particles.add(new Particle(i, j));
    }
  }
}

void draw(){
  for (Particle p: particles){
    p.update();
    p.display();
  }
}

class Particle{
  
  PVector position;
  PVector prevPosition;
  PVector velocity;
  float noiseValue;
  
  Particle(float X, float Y){
    position = new PVector(X, Y);
    prevPosition = new PVector(X, Y);
    velocity = new PVector(0, 0);
  }
  
  void update(){
    if (position.x > width | position.x < 0 | position.y > height | position.y < 0){
      position = new PVector(random(width), random(height));
    }
    noiseValue = noise(position.x * l, position.y * l);
    prevPosition = position;
    velocity = PVector.fromAngle(noiseValue * 24 * PI);
    velocity.setMag(speed);
    position.add(PVector.div(velocity, frameRate));
  }
  
  void display(){
    stroke((noiseValue * 255 * 2) % 255, 255, 255, 30);
    line(position.x, position.y, prevPosition.x, prevPosition.y);
  }
  
}

void keyPressed(){
  if (key == ' '){
    saveFrame("img/screen-####.jpg");
  }
}
