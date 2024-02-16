package com.example.demo.service;

import org.springframework.stereotype.Service;
import reactor.core.publisher.Mono;
import java.time.Duration;

@Service
public class HelloWorldService {

    public Mono<String> getHelloWorld() {
        // Simulate a delay, e.g., fetching data from a remote service
        return Mono.just("Hello World").delayElement(Duration.ofSeconds(2));
    }
}
