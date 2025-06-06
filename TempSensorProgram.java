import java.util.ArrayList;
import java.util.List;

// observer interface
interface Observer {
    void update(float temperature);
}

// subject interface
interface Subject {
    void addObserver(Observer o);
    void removeObserver(Observer o);
    void notifyObservers();
}

// TemperatureSensor sebagai Subject
class TemperatureSensor implements Subject {
    private List<Observer> observers;
    private float temperature;

    public TemperatureSensor() {
        observers = new ArrayList<>();
    }

    @Override
    public void addObserver(Observer o) {
        observers.add(o);
    }

    @Override
    public void removeObserver(Observer o) {
        observers.remove(o);
    }

    @Override
    public void notifyObservers() {
        for (Observer o : observers) {
            o.update(temperature);
        }
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
        notifyObservers();
    }
}

// observer 1 - show current temperature
class CurrentConditionDisplay implements Observer {
    @Override
    public void update(float temperature) {
        System.out.println("Current temperature : " + temperature + "°C");
    }
}

// observer 2 - show temperature statistics
class StatisticsDisplay implements Observer {
    private float maxTemp = Float.MIN_VALUE;
    private float minTemp = Float.MAX_VALUE;
    private float totalTemp = 0;
    private int count = 0;

    @Override
    public void update(float temperature) {
        totalTemp += temperature;
        count++;

        if (temperature > maxTemp) maxTemp = temperature;
        if (temperature < minTemp) minTemp = temperature;

        float avg = totalTemp / count;
        System.out.println("Avg/Max/Min temperature: " + avg + "/" + maxTemp + "/" + minTemp + "°C");
    }
}

// main program
public class TempSensorProgram {
    public static void main(String[] args) {
        TemperatureSensor sensor = new TemperatureSensor();

        Observer currentDisplay = new CurrentConditionDisplay();
        Observer statsDisplay = new StatisticsDisplay();

        sensor.addObserver(currentDisplay);
        sensor.addObserver(statsDisplay);

        sensor.setTemperature(25.5f);
        sensor.setTemperature(27.0f);
        sensor.setTemperature(23.3f);
    }
} 