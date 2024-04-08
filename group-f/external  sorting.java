// Assume we have two input and two output tapes to perform the sorting. The internal 
// memory can hold and sort m records at a time. Write a program in java for external 
// sorting. Find out time complexity. 

import java.io.*;
import java.util.*;

public class ExternalSorting {
    // Merge function to merge two sorted arrays
    private static void merge(int[] arr, int l, int m, int r) {
        int n1 = m - l + 1;
        int n2 = r - m;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; ++i)
            L[i] = arr[l + i];
        for (int j = 0; j < n2; ++j)
            R[j] = arr[m + 1 + j];

        int i = 0, j = 0;
        int k = l;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    // External merge sort function
    private static void externalMergeSort(int[] arr, int l, int r, int m) {
        if (l < r) {
            if (r - l <= m) { // If number of elements is less than or equal to the memory size
                Arrays.sort(arr, l, r + 1);
            } else {
                int mid = l + (r - l) / 2;
                externalMergeSort(arr, l, mid, m);
                externalMergeSort(arr, mid + 1, r, m);
                merge(arr, l, mid, r);
            }
        }
    }

    // Main function for external sorting
    public static void externalSort(int[] arr, int memorySize) {
        int n = arr.length;

        // Dividing the array into chunks of size 'memorySize'
        for (int i = 0; i < n; i += memorySize) {
            int left = i;
            int right = Math.min(i + memorySize - 1, n - 1);
            externalMergeSort(arr, left, right, memorySize);
        }

        // Merging the sorted chunks
        int chunkSize = memorySize;
        while (chunkSize < n) {
            for (int i = 0; i < n; i += 2 * chunkSize) {
                int left = i;
                int mid = i + chunkSize - 1;
                int right = Math.min(i + 2 * chunkSize - 1, n - 1);
                merge(arr, left, mid, right);
            }
            chunkSize *= 2;
        }
    }

    // Utility function to print an array
    private static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6, 7};
        int memorySize = 2; // Internal memory size

        System.out.println("Original array:");
        printArray(arr);

        externalSort(arr, memorySize);

        System.out.println("\nSorted array:");
        printArray(arr);
    }
}
