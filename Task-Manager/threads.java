class MinhaThread extends Thread {
    private String nome;
    private int delay;

    public MinhaThread(String nome, int delay) {
        this.nome = nome;
        this.delay = delay;
    }

    @Override
    public void run() {
        for (int i = 0; i < 5; i++) {
            try {
                Thread.sleep(delay);
                System.out.println(nome + ": Iteração " + (i + 1));
            } catch (InterruptedException e) {
                System.out.println(nome + " foi interrompida.");
            }
        }
    }

    public static void main(String[] args) {
        MinhaThread thread1 = new MinhaThread("Thread-1", 1000);
        MinhaThread thread2 = new MinhaThread("Thread-2", 500);
        MinhaThread thread3 = new MinhaThread("Thread-3", 300);

        thread1.start();
        thread2.start();
        thread3.start();

        try {
            thread1.join();
            thread2.join();
            thread3.join();
        } catch (InterruptedException e) {
            System.out.println("A execução principal foi interrompida.");
        }

        System.out.println("Execução de todas as threads concluída.");
    }
}
