// Implement the Heap/Shell sort algorithm implemented in Java demonstrating heap/shell 
// data structure with modularity of programming language 


import java.util.Arrays;

public class SortingAlgorithms {
    
    // Heap Sort Algorithm
    
    public static void heapSort(int[] arr) {
        int n = arr.length;
        
        // Build max heap
        for (int i = n / 2 - 1; i >= 0; i--)
            heapify(arr, n, i);
        
        // Heap sort
        for (int i = n - 1; i > 0; i--) {
            // Swap root (maximum element) with last element
            int temp = arr[0];
            arr[0] = arr[i];
            arr[i] = temp;
            
            // Heapify root element
            heapify(arr, i, 0);
        }
    }
    
    private static void heapify(int[] arr, int n, int i) {
        int largest = i; // Initialize largest as root
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        // If left child is larger than root
        if (left < n && arr[left] > arr[largest])
            largest = left;
        
        // If right child is larger than largest so far
        if (right < n && arr[right] > arr[largest])
            largest = right;
        
        // If largest is not root
        if (largest != i) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;
            
            // Recursively heapify the affected sub-tree
            heapify(arr, n, largest);
        }
    }
    
    // Shell Sort Algorithm
    
    public static void shellSort(int[] arr) {
        int n = arr.length;
        
        // Start with a big gap, then reduce the gap
        for (int gap = n/2; gap > 0; gap /= 2) {
            // Do a gapped insertion sort for this gap size.
            // The first gap elements arr[0..gap-1] are already in gapped order
            // keep adding one more element until the entire array is gap sorted
            for (int i = gap; i < n; i++) {
                // add arr[i] to the elements that have been gap sorted
                // save arr[i] in temp and make a hole at position i
                int temp = arr[i];
                
                // shift earlier gap-sorted elements up until the correct location for arr[i] is found
                int j;
                for (j = i; j >= gap && arr[j - gap] > temp; j -= gap)
                    arr[j] = arr[j - gap];
                
                // put temp (the original arr[i]) in its correct location
                arr[j] = temp;
            }
        }
    }
    
    // Helper method to print array
    public static void printArray(int[] arr) {
        System.out.println(Arrays.toString(arr));
    }
    
    // Main method to test sorting algorithms
    public static void main(String[] args) {
        int[] arr1 = {12, 11, 13, 5, 6, 7};
        int[] arr2 = {12, 11, 13, 5, 6, 7};
        
        System.out.println("Original Array:");
        printArray(arr1);
        
        heapSort(arr1);
        System.out.println("Array after Heap Sort:");
        printArray(arr1);
        
        shellSort(arr2);
        System.out.println("Array after Shell Sort:");
        printArray(arr2);
    }
}
