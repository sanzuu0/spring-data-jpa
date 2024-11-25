package com.szu.springdatajpa.entity;


import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.util.List;

@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name = "person", schema = "public", catalog = "data-jpa")
@Entity
public class PersonEntity {
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id", nullable = false)
    Long id;

    @Basic
    @Column(name = "email", nullable = false, length = 100)
    String email;

    @Basic
    @Column(name = "first_name", nullable = false, length = 100)
    String firstName;

    @Basic
    @Column(name = "last_name", nullable = false, length = 100)
    String lastName;

    @Basic
    @Column(name = "phone_number", nullable = false, length = 100)
    private String phoneNumber;

    @OneToMany(mappedBy = "person")
    @ToString.Exclude
    @EqualsAndHashCode.Exclude
    List<JobHistoryEntity> jobHistories;
}
