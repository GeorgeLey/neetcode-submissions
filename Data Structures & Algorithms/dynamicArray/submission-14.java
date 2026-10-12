class DynamicArray {

    public int[] arr;
    public int size;

    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.size = 0;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        int i = this.size;
        if (this.size == this.arr.length) {
            resize();
        }
        this.arr[i] = n;
        this.size++;
    }

    public int popback() {
        this.size--;
        return this.arr[this.size];
    }

    private void resize() {
        int[] bigger = new int[2*this.arr.length];
        int i = 0;
        for (int num : arr) {
            bigger[i] = num;
            i++;
        }
        this.arr = bigger;
    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.arr.length;
    }
}
