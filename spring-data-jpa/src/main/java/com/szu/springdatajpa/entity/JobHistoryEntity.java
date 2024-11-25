package com.szu.springdatajpa.entity;


import jakarta.persistence.*;
import lombok.*;
import lombok.experimental.FieldDefaults;

import java.time.LocalDate;


@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor
@FieldDefaults(level = AccessLevel.PRIVATE)
@Table(name = "job_history", schema = "public", catalog = "data-jpa")
@Entity
public class JobHistoryEntity {
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Id
    @Column(name = "id", nullable = false)
    Long id;

    @Basic
    @Column(name = "date_from", nullable = true)
    LocalDate dateFrom;

    @Basic
    @Column(name = "date_to", nullable = true)
    LocalDate dateTo;

    @Basic
    @Column(name = "salary", nullable = true)
    Integer salary;

    @ManyToOne
    @JoinColumn(name = "job_id", referencedColumnName = "id")
    JobEntity job;

    @ManyToOne
    @JoinColumn(name = "person_id", referencedColumnName = "id")
    PersonEntity person;
}
