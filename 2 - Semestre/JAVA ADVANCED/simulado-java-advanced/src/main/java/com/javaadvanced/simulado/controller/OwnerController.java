package com.javaadvanced.simulado.controller;

import com.javaadvanced.simulado.entity.Blog;
import com.javaadvanced.simulado.entity.Owner;
import com.javaadvanced.simulado.repository.BlogRepository;
import com.javaadvanced.simulado.repository.OwnerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Collection;
import java.util.NoSuchElementException;
import java.util.Optional;

@CrossOrigin(maxAge = 3600)
@RestController
@RequestMapping("api/owner")
public class OwnerController {

    @Autowired
    private OwnerRepository ownerRepository;
    @Autowired
    private BlogRepository blogRepository;

    @PostMapping("/create")
    public Owner saveOwner(@RequestBody Owner owner) {
        System.out.println("Owner save called...");
        Owner ownerOut = ownerRepository.save(owner);
        System.out.println("Saved!!!");

        return ownerOut;
    }

    @PutMapping("/update/{id}")
    public Owner updateOwner(@RequestBody Owner ownerRequest, @PathVariable int id){
        Owner owner = ownerRepository.findById(id)
                .orElseThrow(() -> new NoSuchElementException("Owner não encontrado !!"));
        owner.setEmail(ownerRequest.getEmail());
        owner.setName(ownerRequest.getName());

        ownerRepository.save(owner);
        return owner;
    }

    @DeleteMapping("/delete/{id}")
    public ResponseEntity<String> deleteOwner(@PathVariable int id){
        ownerRepository.deleteById(id);
        return ResponseEntity.ok("Owner deletado com sucesso !!");
    }

    @GetMapping("/get/{id}")
    public Optional<Owner> getOwner(@PathVariable String id) {
        System.out.println("Owner get() called...");
        Optional<Owner> outOwner = ownerRepository.findById(Long.valueOf(id));
        System.out.println("Owner with Engine :: " + outOwner);

        return outOwner;
    }

    @GetMapping("/getByEmail/{email}")
    public Optional<Owner> getOwnerByEmail(@PathVariable String email) {
        Optional<Owner> outOwner = ownerRepository.findByEmail(email);
        return outOwner;
    }

    @GetMapping("/getByName/{name}")
    public Optional<Owner> getOwnerByName(@PathVariable String name) {
        Optional<Owner> outOwner = ownerRepository.findByName(name);
        return outOwner;
    }

    @GetMapping("/getAllBlogs")
    public Page<Blog> findAllBlogs(@RequestParam(defaultValue = "10") int size, @RequestParam(defaultValue = "0") int pageNumber) {
        Pageable pageable = PageRequest.of(pageNumber, size);
        return blogRepository.findAll(pageable);
    }

    @GetMapping("/getAllOwners")
    public Page<Owner> findAllOwners(@RequestParam(defaultValue = "10") int size, @RequestParam(defaultValue = "0") int pageNumber) {
        Pageable pageable = PageRequest.of(pageNumber, size);
        return ownerRepository.findAll(pageable);
    }

    @GetMapping("/jpqltest/{title}")
    public Collection<Blog> getBlogsByTitle(@PathVariable String title) {
        System.out.println("Owner get() called...");
        Collection<Blog> outOwner = blogRepository.getBlogsByTitleNative(title);
        //Collection<Blog> outOwner = blogRepository.jpqlTest1(title);
        System.out.println("Owner with Engine :: " + outOwner);

        return outOwner;
    }

    @GetMapping("/querytest/{param}")
    public Collection<Owner> queryTest(@PathVariable String param) {
        return ownerRepository.findByNameNot(param);
    }
}