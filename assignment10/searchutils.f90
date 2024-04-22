module searchutils
    implicit none
    

contains

! Description: Function that finds the location (idx) of a value x
! in an array using the linear search algorithm.
!
! Find idx such that arr(idx) == x
!
FUNCTION linearSearch(arr, n, x) RESULT(idx)
 use omp_lib
 IMPLICIT NONE

 REAL(8) :: arr(n) ! Array to search
 INTEGER :: n ! Number of elements in array.
 REAL(8) :: x ! Value to search for in array.
 INTEGER :: idx ! Result of the search. [arr(idx) == x]

 ! Your implementation here.

 INTEGER :: i
        
        !set idx to -1 in case element is not found.
    idx = -1 

    !$omp parallel private(i)
    !$omp do
    DO i = 1, n
        IF (arr(i) == x) THEN
            !$omp critical
                !update idx if element is found
            idx = i 
            !$omp end critical
            ! EXIT
        END IF
    END DO
    !$omp end do
    !$omp end parallel




END FUNCTION linearSearch
! Description: Function that finds the location (idx) of a value x
! in a sorted array using the binary search algorithm.
!
! Find idx such that arr(idx) == x
!
FUNCTION binarySearch(arr, n, x) RESULT(idx)

 IMPLICIT NONE

 REAL(8) :: arr(n) ! Array to search
 INTEGER :: n ! Number of elements in array.
 REAL(8) :: x ! Value to search for in array.
 INTEGER :: idx ! Result of the search. [arr(idx) == x]

 ! Your implementation here.
 INTEGER :: low, high, mid
    
    low = 1
    high = n
    idx = -1
    
    !binary search
    DO WHILE (low <= high)
        mid = (low + high) / 2
        IF (arr(mid) == x) THEN
            idx = mid
            EXIT
        ELSE IF (arr(mid) < x) THEN
            low = mid + 1
        ELSE
            high = mid - 1
        END IF
    END DO



END FUNCTION binarySearch


end module searchutils
