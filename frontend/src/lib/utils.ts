import { type ClassValue, clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

/**
 * Merge class names, letting later Tailwind utilities win over earlier ones.
 *
 * clsx flattens the conditional/array/object forms; twMerge then resolves
 * conflicts within the same Tailwind group, so `cn('p-2', 'p-4')` yields `p-4`
 * instead of emitting both and leaving the outcome to stylesheet order.
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}
