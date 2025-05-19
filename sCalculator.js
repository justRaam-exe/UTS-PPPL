// Add Operation
class AddOperation {
    execute(a, b){
        return a + b;
    }
}

// Subtract Operation
class SubtractOperation {
    execute(a, b){
        return a - b;
    }
}

// Multiply Operation
class MultiplyOperation {
    execute(a, b){
        return a * b;
    }
}

// Divide Operation
class DivideOperation {
    execute(a, b){
        if (b === 0){
            throw new Error("Tidak bisa dibagi dengan nol");
        }
        return a / b;
    }
}

class calculator {
    setStrategy(strategy) {
        this.strategy = strategy;
    }

    calculate(a, b){
        if (!this.strategy) {
            throw new Error("Strategy belum ditentukan");
        }
        return this.strategy.execute(a, b);
    }
}

const calc = new calculator();

calc.setStrategy(new AddOperation());
console.log("45 + 15 = " + calc.calculate(45, 15));

calc.setStrategy(new SubtractOperation())
console.log("10 - 5 = " + calc.calculate(10, 5));

calc.setStrategy(new MultiplyOperation());
console.log("55 x 12 = " + calc.calculate(55, 12));

calc.setStrategy(new DivideOperation());
console.log("45 / 5 = " + calc.calculate(45, 5));