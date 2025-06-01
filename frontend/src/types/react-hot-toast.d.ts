declare module 'react-hot-toast' {
  const toast: {
    (message: string): void;
    success(message: string): void;
    error(message: string): void;
  };
  
  export function Toaster(props: { 
    position?: 'top-center' | 'top-right' | 'top-left' | 'bottom-center' | 'bottom-right' | 'bottom-left' 
  }): JSX.Element;
  
  export default toast;
} 